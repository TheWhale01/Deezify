<script lang="ts">
	import { goto } from "$app/navigation";
</script>

<h2>Create Party</h2>
<button on:click={() => goto('/create')}>Create Party</button>

<h2>Join Party</h2>
<button on:click={() => goto('/join')}>Join Party</button>
