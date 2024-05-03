import React, { useState, useEffect } from "react";
import axios from "axios";

export default function SellerDashboardLottery() {
  const [errorMessage, setErrorMessage] = useState(null);
  const [lotteryItems, setLotteryItems] = useState(null);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      if (JSON.parse(localStorage.getItem("user_data")).type === "bidder") {
        setErrorMessage("Only sellers are allowed.");
      }

      async function fetchData() {
        await axios
          .get("/seller/dashboard/lottery/")
          .then((res) => {
            setLotteryItems(res.data);
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
            Posted Lottery Items
          </h2>

          <div class="my-6">
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
