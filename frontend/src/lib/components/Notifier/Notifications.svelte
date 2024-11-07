<script lang="ts">
	import { getNotification } from '$lib/components/Notifier/Notifier.svelte';
	import Notif from './Notif.svelte';

	const notifier = getNotification();
</script>

<div class="absolute flex flex-col top-[5%] right-[5%] h-screen w-[10%]">
	{#each notifier.notifications as notif }
		<Notif notif={ notif }></Notif>
	{/each }
</div>
