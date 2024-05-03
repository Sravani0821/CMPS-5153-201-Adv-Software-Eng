import { useEffect, useState } from "react";
import axios from "axios";

export default function Notifications() {
  const [notifications, setNotifications] = useState([]);

  async function getNotifications() {
    try {
      const response = await axios.get("/item/notifications/");
      setNotifications(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      getNotifications();
    } else {
      window.location.href = "/login";
    }
  }, []);

  return (
    <div class="mx-auto max-w-2xl px-4 py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900">
        Notifications
      </h2>

      {notifications.length > 0 ? (
        <div class="mt-6">
          {notifications.map((notification) => (
            <div class="bg-white shadow overflow-hidden sm:rounded-lg mt-4">
              <div class="px-4 py-5 sm:px-6">
                <h3 class="text-lg font-medium text-gray-900">
                  {notification.title}
                </h3>
                <p class="mt-1 max-w-2xl text-sm text-gray-500">
                  {notification.message}
                </p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div class="mt-6">
          <p class="text-sm text-gray-500">No notifications available.</p>
        </div>
      )}
    </div>
  );
}
