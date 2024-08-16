<script lang="ts">
	import { play_state } from "$lib/store.svelte";
	import PlayState from "$lib/enums/play_state";
	import PlayerIcon from "./PlayerIcon.svelte";
</script>

<div class="bg-sky-500 w-full flex justify-evenly">
	<PlayerIcon icon="fa-backward" />
	{#if play_state.value == PlayState.PAUSED }
		<PlayerIcon icon="fa-ply" />
	{:else }
		<PlayerIcon icon="fa-pause" />
	{/if }
	<PlayerIcon icon="fa-forward" />
</div>
