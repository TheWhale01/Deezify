<script lang="ts">
	const { children } = $props();
</script>

<div class="flex flex-col justify-between items-center h-full w-full">
	{@render children()}
</div>
