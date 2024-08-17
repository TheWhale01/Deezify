<script lang="ts">
	import { goto } from "$app/navigation";
	import { getUser } from "$lib/store.svelte";

	getUser().get_me();
</script>

<button on:click={() => goto('/create')}>Create Party</button>
<button on:click={() => goto('/join')}>Join Party</button>
