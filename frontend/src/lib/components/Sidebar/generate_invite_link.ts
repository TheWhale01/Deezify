export default function generate_invite_link() {
	let url: string = window.location + "/add_user";
	navigator.clipboard.writeText(url);
}
