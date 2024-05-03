import React, { useState, useEffect } from "react";
import axios from "axios";

export default function SellerDashboard() {
  const [errorMessage, setErrorMessage] = useState(null);
  const [storeItems, setStoreItems] = useState(null);
  const [lotteryItems, setLotteryItems] = useState(null);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      if (JSON.parse(localStorage.getItem("user_data")).type === "bidder") {
        setErrorMessage("Only sellers are allowed.");
      }

      async function fetchData() {
        await axios
          .get("/seller/dashboard/")
          .then((res) => {
            setStoreItems(res.data.recent_store_items);
            setLotteryItems(res.data.recent_lottery_items);
          })
          .catch((err) => {
            console.log(err);
          });
      }

      fetchData();
    } else {
      window.location.href = "/login";
    }
  }, []);

  return (
    <>
      {errorMessage ? (
        <div className="text-center text-red-500">{errorMessage}</div>
      ) : (
        <div class="mx-auto max-w-2xl px-4 py-10 sm:px-6 lg:max-w-7xl lg:px-8">
          <h2 class="text-2xl font-bold tracking-tight text-gray-900">
            Seller Dashboard
          </h2>

          <div class="my-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
            <a
              href="/store/create/"
              class="flex flex-col items-center justify-center p-6 text-center text-gray-900 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md"
            >
              <svg
                class="w-12 h-12 text-gray-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                ></path>
              </svg>
              <span class="mt-4 text-lg font-medium">Post New Store Item</span>
            </a>

            <a
              href="/dashboard/seller/store/"
              class="flex flex-col items-center justify-center p-6 text-center text-gray-900 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md"
            >
              <svg
                class="w-12 h-12 text-gray-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                ></path>
              </svg>
              <span class="mt-4 text-lg font-medium">
                View Posted Store Items
              </span>
            </a>

            <a
              href="/lottery/create/"
              class="flex flex-col items-center justify-center p-6 text-center text-gray-900 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md"
            >
              <svg
                class="w-12 h-12 text-gray-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                ></path>
              </svg>
              <span class="mt-4 text-lg font-medium">
                Create New Lottery Item
              </span>
            </a>

            <a
              href="/dashboard/seller/lottery/"
              class="flex flex-col items-center justify-center p-6 text-center text-gray-900 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md"
            >
              <svg
                class="w-12 h-12 text-gray-500"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                ></path>
              </svg>
              <span class="mt-4 text-lg font-medium">
                View Posted Lottery Items
              </span>
            </a>
          </div>

          <div class="my-6">
            <h2 class="text-lg font-bold tracking-tight text-gray-900">
              Recently Posted Store Items
            </h2>

            <table class="mt-4 w-full border border-gray-200 rounded-lg">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Title
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Opening Bid
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Action End Date
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    View
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 text-center">
                {storeItems &&
                  storeItems.map((item) => (
                    <tr>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        {item.title}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        ${item.opening_bid}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        {new Date(item.auction_end).toLocaleString()}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <a
                          href={`/store/item/${item.id}`}
                          class="text-blue-500 hover:underline"
                        >
                          View
                        </a>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>

          <div class="my-6">
            <h2 class="text-lg font-bold tracking-tight text-gray-900">
              Recently Posted Lottery Items
            </h2>

            <table class="mt-4 w-full border border-gray-200 rounded-lg">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Title
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Bid
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    View
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 text-center">
                {lotteryItems &&
                  lotteryItems.map((item) => (
                    <tr>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        {item.title}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        ${item.bid}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <a
                          href={`/lottery/item/${item.id}`}
                          class="text-blue-500 hover:underline"
                        >
                          View
                        </a>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </>
  );
}
