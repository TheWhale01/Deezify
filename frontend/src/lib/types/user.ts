import Services from "$lib/enums/services";

export default interface User {
	id: number;
	username: string;
	token: string;
	service: Services; 
	party_id: number;
}
