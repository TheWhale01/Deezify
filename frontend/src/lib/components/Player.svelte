<script lang="ts">
	import PlayState from "$lib/enums/play_state";
	import PlayerIcon from "./PlayerIcon.svelte";
	import { getPlayer } from "$lib/store.svelte";
</script>

<div class="bg-sky-500 w-full flex justify-evenly sticky bottom-0">
	<PlayerIcon icon="fa-backward" />
	{#if getPlayer().state === PlayState.PAUSED }
		<PlayerIcon icon="fa-play" />
	{:else }
		<PlayerIcon icon="fa-pause" />
	{/if }
	<PlayerIcon icon="fa-forward" />
</div>
