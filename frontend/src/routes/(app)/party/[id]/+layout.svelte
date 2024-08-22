<script lang="ts">
	import { setPlayer } from '$lib/store.svelte';
	const { children } = $props();

	setPlayer();
</script>

<div class="flex flex-col justify-between items-center h-full w-full">
	{@render children()}
</div>
