<script lang="ts">
	import { getNotification } from '$lib/components/Notifier/Notifier.svelte';
	import Notif from './Notif.svelte';

	const notifier = getNotification();
</script>

<div class="absolute flex flex-col top-[5%] max-h-[95vh] right-[5%] w-[10%] overflow-hidden">
	{#each notifier.notifications as notif }
		<Notif notif={ notif }></Notif>
	{/each }
</div>
