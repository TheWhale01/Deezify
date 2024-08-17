import Services from "$lib/enums/services";

export default interface UserType {
  id: number;
  username: string;
  token: string;
  service: Services;
  party_id: number | null;
  owner: boolean;
  logged: boolean;
}
