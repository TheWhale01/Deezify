<script lang="ts">
	import PlayState from "$lib/enums/play_state";
	import PlayerIcon from "./PlayerIcon.svelte";
	import { getPlayer } from "$lib/store.svelte";
    	import env from "$lib/env";

	const player = getPlayer();
	async function play(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/song/init_playback`, {
			method: "PUT",
			credentials: 'include'
		});
		if (response.status !== 200)
			return ;
	}

	async function pause(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + '/song/pause', {
			method: 'PUT',
			credentials: 'include',
		});
		if (response.status !== 200)
			return ;
	}
</script>

<div class="bg-neutral-200 w-full flex justify-evenly sticky bottom-0 mt-4">
	<PlayerIcon icon="fa-backward"/>
	{#if player.state === PlayState.PAUSED }
		<PlayerIcon icon="fa-play" on:click={play}/>
	{:else }
		<PlayerIcon icon="fa-pause" on:click={pause}/>
	{/if }
	<PlayerIcon icon="fa-forward" />
</div>
