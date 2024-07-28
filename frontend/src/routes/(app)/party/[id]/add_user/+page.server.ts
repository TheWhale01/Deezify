import env from "$lib/env";
import { redirect } from "@sveltejs/kit";

export async function load({ params, cookies }: any) {
	const cookie_string: string = `access_token=${cookies.get("access_token")}`;
	const response = await fetch(
		env.SERVER_BACKEND_URL + `/party/${params.id}/add_user`,
		{
			method: "PUT",
			headers: {
				Cookie: cookie_string,
			},
		},
	);
	if (response.status !== 200) return;
	throw redirect(302, `/party/${params.id}`);
}
