<script lang="ts">
	import type Party from "$lib/types/party";
	import env from "$lib/env";
	import { goto } from "$app/navigation";
	import type SearchResult from "$lib/types/search_results";

	export let data: Party;
	export let form: any;

	const results: SearchResult[] | null = form?.data;
	async function delete_party(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/party/${data.id}`, {
			method: "DELETE",
			credentials: "include",
		});
		if (response.status !== 200) return;
		goto("/");
	}

	async function add_to_queue(item: SearchResult): Promise<void> {
		console.log(item);
	}

	function generate_invite_link() {
		let url: string = window.location + "/add_user";
		navigator.clipboard.writeText(url);
		alert("Invite link copied to clipboard");
	}
</script>

<h2>Party</h2>

<form method="post">
	<input type="text" placeholder="Search" name="search" />
	<button type="submit">Search</button>
</form>

{#if results}
	<div>
		<ul>
			{#each results as item}
				<li>
					<button on:click={() => add_to_queue(item)}>
						<span>{item.id}</span>
						<span>{item.title}</span>
						<span>{item.artist}</span>
						<img src={item.cover} alt="album cover" />
					</button>
				</li>
			{/each}
		</ul>
	</div>
{/if}

{#if data.owner}
	<button on:click={delete_party}>Delete</button>
	<button on:click={generate_invite_link}>Generate invite link</button>
{/if }

