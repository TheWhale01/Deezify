<script lang="ts">
	import { goto } from "$app/navigation";
</script>

<button on:click={() => goto('/create')}>Create Party</button>
<button on:click={() => goto('/join')}>Join Party</button>
