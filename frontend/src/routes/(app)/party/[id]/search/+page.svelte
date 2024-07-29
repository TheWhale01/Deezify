<script lang="ts">
	import type SearchResult from "$lib/types/search_results";
	import SearchResults from "$lib/components/SearchResults.svelte";

	export let form: any;

	const results: SearchResult[] | null = form?.data;
</script>

<div class="flex flex-col justify-between items-center h-full w-full">
	<form method="post" class='p-4 w-full flex-row'>
		<input type="text" placeholder="Search" name="search" class="mr-2 w-full p-2"/>
		<button type="submit">Search</button>
	</form>

	<div class="h-full flex flex-col items-center overflow-scroll w-full p-2">
		{#if results}
			<SearchResults results={results} />
		{/if}
	</div>
</div>
