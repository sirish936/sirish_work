package com.sirish.inner;

public class Test {
	public static void main(final String[] args) {
		final State st = new State();
		System.out.println(st.getValue());
		final State.Momento mem = st.momento();
		st.alterValue();
		System.out.println(st.getValue());
		mem.restore();
		System.out.println(st.getValue());
	}

	public static class State {
		protected int val = 11;

		int getValue() {
			return val;
		}

		void alterValue() {
			val = (val + 7) % 31;
		}

		Momento momento() {
			return new Momento();
		}

		class Momento {
			int val;

			Momento() {
				this.val = State.this.val;
				System.out.println(val);
			}

			void restore() {
				State.this.val = val;
			}
		}
	}
}