import { useEffect, useState } from "react";

export default function Home() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    if (localStorage.getItem("user_data")) {
      setUserData(JSON.parse(localStorage.getItem("user_data")));
    }
  }, []);

  return (
    <div className="p-5">
      <h3>Hi {userData && `( ${userData.type} )`}</h3>
      {userData && (
        <ul>
          <li>
            Id: <b>{userData.data.id}</b>
          </li>
          <li>
            Slug: <b>{userData.data.slug}</b>
          </li>
          <li>
            First Name: <b>{userData.data.first_name}</b>
          </li>
          <li>
            Last Name: <b>{userData.data.last_name}</b>
          </li>
          <li>
            Email: <b>{userData.data.email}</b>
          </li>
        </ul>
      )}
    </div>
  );
}
