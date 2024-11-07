<script lang="ts">
	import env from "$lib/env";
	import type SearchResult from "$lib/types/search_results";
	import SearchResults from "$lib/components/SearchResults.svelte";

	let query: string = $state('');

	let results: SearchResult[] = $state([]);

	async function search(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/search?q=${query}`, {
			method: 'GET',
			credentials: 'include'	
		});
		if (response.status !== 200)
			return ;
		const response_json = await response.json();
		results = response_json['data'];
	}

</script>

<form on:submit|preventDefault={search} class='p-4 w-full flex-row'>
	<input type="text" placeholder="Search" name="search" class="mr-2 w-full p-2" bind:value={query}/>
	<button type="submit">Search</button>
</form>

<div class="h-full flex flex-col items-center overflow-scroll w-full p-2">
	{#if results.length}
		<SearchResults results={results} />
	{/if}
</div>
