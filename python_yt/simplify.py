if response_body is not None and response_status == 200:
            task_state = response_body[TASK_STATE]
            self.logger.info(
                "task_state : %s, for task_uri : %s, for jobId : %s.",
                task_state,
                context.data.get(URI),
                context.job_id,
            )
            if task_state == OVTaskState.completed:
                step_finished = True
                raise JobDoneException(
                    "Server successfully powered off."
                )
        elif response_body is not None and response_status != 200:
            task_state = response_body[TASK_STATE]
            self.logger.info(
                "task_state : %s, for task_uri : %s, for jobId : %s.",
                task_state,
                context.data.get(URI),
                context.job_id,
            )
            if task_state == OVTaskState.error:
                raise JobErrorException("Power off failed")
        else:
            task_state = response_body[TASK_STATE]
            self.logger.info(
                "task_state : %s, for task_uri : %s, for jobId : %s.",
                task_state,
                context.data.get(URI),
                context.job_id,
            )
            if task_state not in [OVTaskState.completed, OVTaskState.error]:
                raise JobRetryWithContinueException()