import { useEffect, useState } from "react";
import axios from "axios";
import StoreItemCard from "./store-item-card";

export default function StoreHome() {
  const [storeItems, setStoreItems] = useState(null);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      async function fetchStoreItems() {
        await axios
          .get("/item/store/")
          .then((res) => {
            console.log(res.data);
            setStoreItems(res.data);
          })
          .catch((err) => {
            console.log(err);
          });
      }
      fetchStoreItems();
    } else {
      window.location.href = "/login";
    }
  }, []);

  return (
    <div class="mx-auto max-w-2xl px-4 py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900">
        Store Items
      </h2>

      {storeItems && (
        <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          {storeItems.map((item) => (
            <StoreItemCard key={item.id} item={item} />
          ))}
        </div>
      )}
    </div>
  );
}
