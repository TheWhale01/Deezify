import env from "$lib/env";
import { redirect } from "@sveltejs/kit";

export const handle = async ({ event, resolve }: any) => {
	const token: string | undefined = event.cookies.get("access_token");
	const cookie_string: string = `access_token=${token}`;
	let party_id: number | null = null;

	const user_response = await fetch(env.SERVER_BACKEND_URL + "/user/me", {
		method: "GET",
		headers: {
			Cookie: cookie_string,
		},
	});
	const valid_token: boolean = user_response.status === 200;

	const party_response = await fetch(env.SERVER_BACKEND_URL + '/user/party', {
		method: 'GET',
		headers: {
			Cookie: cookie_string
		}
	});

	if (party_response.status === 200) {
		const party_json = await party_response.json();
		if (party_json)
			party_id = party_json['id'];
	}
	if (!valid_token) {
		event.cookies.delete("access_token", {
			path: "/",
			httpOnly: true,
			samesite: 'none',
			secure: true,
			domain: '.deezify.duckdns.org',
		});
	}

	if (!valid_token && !event.route.id?.startsWith("/login"))
		throw redirect(302, "/login");
	else if (valid_token && !event.route.id?.startsWith("/(app)"))
		throw redirect(302, "/");
	else if (valid_token && party_id && !event.route.id?.startsWith('/(app)/party/[id]'))
		throw redirect(302, `/party/${party_id}`)
	else if (valid_token && !party_id && event.route.id?.startsWith('/(app)/party/[id]'))
		throw redirect(302, '/');
	const response = await resolve(event);
	return response;
};
