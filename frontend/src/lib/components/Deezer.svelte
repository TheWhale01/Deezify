<div id="dz-root"></div>
<script lang="ts">
	import { onMount } from "svelte";

	onMount(() => {
		window.dzAsyncInit = () => initDeezerPlayback();
		const script = document.createElement('script');
		script.src = 'https://e-cdn-files.dzcdn.net/js/min/dz.js';
		document.body.prepend(script);
	});

	function initDeezerPlayback() {
		DZ.init({
			appId  : '601764',
			channelUrl : 'https://deezify.duckdns.org/deezer/channel',
			player: {
				onload: (response) => {console.log(response);},
			}
		});

		DZ.ready((sdk_options) => {
			console.log(sdk_options);	
		});
	}
</script>
