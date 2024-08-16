import PlayState from "./enums/play_state";

export function rune<T>(init_value: T) {
  let value: T = $state(init_value);

  return {
    get value() {
      return value;
    },
    set value(v: T) {
      value = v;
    },
  };
}

export const owner = rune<boolean>(false);
export const logged = rune<boolean>(false);
export const party = rune<boolean>(false);
export const play_state = rune<PlayState>(PlayState.PAUSED);
