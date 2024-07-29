<script lang="ts">
	import ResultCard from '$lib/components/ResultCard.svelte';
	import type SearchResults from '$lib/types/search_results';

	const { results }: { results: SearchResults[] } = $props();
</script>

<div class="h-full overflow-scroll w-full p-2">
	<ul class="flex flex-wrap justify-between">
		{#each results as item}
			<li class='m-2'>
				<ResultCard item={item} />
			</li>
		{/each}
	</ul>
</div>