import env from "$lib/env";
import { redirect } from "@sveltejs/kit";

export const actions = {
	default: async ({ cookies, request }: any) => {
		const data = await request.formData();
		const party_name: string = data.get("partyname");
		const cookie_string: string = `access_token=${cookies.get("access_token")}`;

		const response = await fetch(env.SERVER_BACKEND_URL + "/party/create", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				Cookie: cookie_string,
			},
			body: JSON.stringify({
				name: party_name,
			}),
		});
		if (response.status !== 200) return;
		const response_json = await response.json();
		throw redirect(302, `party/${response_json["id"]}`);
	},
};
