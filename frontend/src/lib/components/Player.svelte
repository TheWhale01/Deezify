<script lang="ts">
	import PlayState from "$lib/enums/play_state";
	import PlayerIcon from "./PlayerIcon.svelte";
	import { getPlayer } from "$lib/store.svelte";

	const playbar = getPlayer();

	async function play(): Promise<void> {
		await playbar.player.resume();
	}

	async function pause(): Promise<void> {
		await playbar.player.pause();
	}
</script>

<div class="bg-slate-200 w-full flex justify-evenly sticky bottom-0">
	<PlayerIcon icon="fa-backward"/>
	{#if playbar.state === PlayState.PAUSED }
		<PlayerIcon icon="fa-play" on:click={play}/>
	{:else }
		<PlayerIcon icon="fa-pause" on:click={pause}/>
	{/if }
	<PlayerIcon icon="fa-forward" />
</div>
