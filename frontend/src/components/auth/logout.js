import { useEffect } from "react";
import axios from "axios";

export default function Logout() {
  useEffect(() => {
    (async () => {
      try {
        await axios.post("/auth/logout/", {
          refresh_token: localStorage.getItem("refresh_token"),
        });
        localStorage.clear();
        axios.defaults.headers.common["Authorization"] = null;
        window.location.href = "/login";
      } catch (e) {
        console.log("logout not working", e);
      }
    })();
  }, []);

  return <></>;
}
