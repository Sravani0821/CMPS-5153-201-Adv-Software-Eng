import React, { useState, useEffect } from "react";
import axios from "axios";

export default function BidderDashboard() {
  const [errorMessage, setErrorMessage] = useState(null);
  const [storeItems, setStoreItems] = useState(null);
  const [lotteryItems, setLotteryItems] = useState(null);
  const [storeItemsPurchased, setStoreItemsPurchased] = useState(null);
  const [lotteryItemsPurchased, setLotteryItemsPurchased] = useState(null);

  async function fetchData() {
    await axios
      .get("/bidder/dashboard/")
      .then((res) => {
        console.log(res.data);
        setStoreItems(res.data.store_items);
        setLotteryItems(res.data.lottery_based_auctions);
        setStoreItemsPurchased(res.data.store_item_purchases);
        setLotteryItemsPurchased(res.data.lottery_based_auction_purchases);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function handleStoreAccept(id) {
    await axios
      .post(`/item/store/${id}/accept/`)
      .then((res) => {
        console.log(res.data);
        fetchData();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function handleStoreReject(id) {
    await axios
      .post(`/item/store/${id}/reject/`)
      .then((res) => {
        console.log(res.data);
        fetchData();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function handleLotteryAccept(id) {
    await axios
      .post(`/item/lottery/${id}/accept/`)
      .then((res) => {
        console.log(res.data);
        fetchData();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function handleLotteryReject(id) {
    await axios
      .post(`/item/lottery/${id}/reject/`)
      .then((res) => {
        console.log(res.data);
        fetchData();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      if (JSON.parse(localStorage.getItem("user_data")).type === "seller") {
        setErrorMessage("Only Bidders are allowed.");
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
            Bidder Dashboard
          </h2>

          <div class="my-6">
            <h2 class="text-lg font-bold tracking-tight text-gray-900">
              Your recent store item bids
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
              Your recent lottery item bids
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

          <div class="my-6">
            <h2 class="text-lg font-bold tracking-tight text-gray-900">
              Your purchased store items
            </h2>

            <table class="mt-4 w-full border border-gray-200 rounded-lg">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Item
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Accept
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Reject
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 text-center">
                {storeItemsPurchased &&
                  storeItemsPurchased.map((item) => (
                    <tr>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        {item.item.title}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <button
                          class="text-blue-500 hover:underline"
                          onClick={() => handleStoreAccept(item.item.id)}
                        >
                          Accept
                        </button>
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <button
                          class="text-blue-500 hover:underline"
                          onClick={() => handleStoreReject(item.item.id)}
                        >
                          Reject
                        </button>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>

          <div class="my-6">
            <h2 class="text-lg font-bold tracking-tight text-gray-900">
              Your purchased lottery items
            </h2>

            <table class="mt-4 w-full border border-gray-200 rounded-lg">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Item
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Accept
                  </th>
                  <th class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Reject
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 text-center">
                {lotteryItemsPurchased &&
                  lotteryItemsPurchased.map((item) => (
                    <tr>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        {item.item.title}
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <button
                          class="text-blue-500 hover:underline"
                          onClick={() => handleLotteryAccept(item.item.id)}
                        >
                          Accept
                        </button>
                      </td>
                      <td class="px-6 py-3 text-sm font-medium text-gray-900">
                        <button
                          class="text-blue-500 hover:underline"
                          onClick={() => handleLotteryReject(item.item.id)}
                        >
                          Reject
                        </button>
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
