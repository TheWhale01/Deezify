<script lang="ts">
	import Sidebar from "$lib/components/Sidebar/Sidebar.svelte";
	import '@fortawesome/fontawesome-free/css/all.min.css'
	import { setUser } from "$lib/store.svelte";
    	import Services from "$lib/enums/services";

	const { children } = $props();
	const user = setUser();

	function import_service_playback(url: string) {
		const script_tag = document.createElement('script');
		script_tag.src = url;
		script_tag.async = true;
		document.body.appendChild(script_tag);
	}

	if (user.owner) {
		let url = '';
		switch (user.service) {
			case Services.SPOTIFY:
				url = 'https://sdk.scdn.co/spotify-player.js';
				break;
			case Services.DEEZER:			
				url = 'https://e-cdn-files.dzcdn.net/js/min/dz.js'
				console.log('Need to instanciate deezer playback sdk');
				break;
			default:
				break; 
		}
		import_service_playback(url);
	}
</script>

<Sidebar/>

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	 {@render children()}
</div>
