package com.sirish.hpe;

public class InstallStateTest {
	InstallState prevInstallState = InstallState.Unknown;

	public void testInstallState() {

		testStates(InstallState.Staging);
		testStates(InstallState.Staging);
		testStates(InstallState.Staging);
		testStates(InstallState.Installing);

	}

	private void testStates(InstallState state) {
		boolean installStateChanged = ((prevInstallState != state) && (prevInstallState != null));
		if(installStateChanged)
		{
			System.out.println("state changed, PrevState "+ prevInstallState);
			System.out.println("NewState "+ state.toString());
		}else{
			System.out.println("state not changed, PrevState "+ prevInstallState);
			System.out.println("NewState "+ state.toString());
		}
		prevInstallState = state;
	}
	
	public static void main(String[] args) {
		InstallStateTest test = new InstallStateTest();
		test.testInstallState();
		
	}

}
