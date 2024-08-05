<script lang="ts">
	import Sidebar from "$lib/components/Sidebar/Sidebar.svelte";
	import '@fortawesome/fontawesome-free/css/all.min.css'
	import { owner } from "$lib/store.svelte";

	const { children } = $props();
</script>

<svelte:head>
{#if owner.value }
	<script src="https://sdk.scdn.co/spotify-player.js"></script>
{/if }
</svelte:head>

<Sidebar/>

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	 {@render children()}
</div>
