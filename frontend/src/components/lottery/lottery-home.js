import { useEffect, useState } from "react";
import axios from "axios";
import LotteryItemCard from "./lottery-item-card";

export default function LottreyHome() {
  const [lottreyItems, setLottreyItems] = useState(null);
  const [allowPost, setAllowPost] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      if (JSON.parse(localStorage.getItem("user_data")).type === "seller") {
        setAllowPost(true);
      }
      async function fetchLottreyItems() {
        await axios
          .get("/item/lottery/")
          .then((res) => {
            console.log(res.data);
            setLottreyItems(res.data);
          })
          .catch((err) => {
            console.log(err);
          });
      }
      fetchLottreyItems();
    } else {
      window.location.href = "/login";
    }
  }, []);

  return (
    <div class="mx-auto max-w-2xl px-4 py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900">
        Lottrey Based Auction Items
      </h2>

      {lottreyItems && (
        <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          {lottreyItems.map((item) => (
            <LotteryItemCard key={item.id} item={item} />
          ))}
        </div>
      )}

      {allowPost && (
        <div class="mt-10 flex items-center justify-center">
          <a
            href="/lottery/create/"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Post New Item
          </a>
        </div>
      )}
    </div>
  );
}
