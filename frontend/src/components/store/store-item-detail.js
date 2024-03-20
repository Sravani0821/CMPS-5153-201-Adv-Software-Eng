import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function StoreItemDetail() {
  const { itemId } = useParams();
  const [storeItem, setStoreItem] = useState(null);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      async function fetchStoreItems() {
        await axios
          .get(`/item/store/${itemId}/`)
          .then((res) => {
            // console.log(res.data);
            setStoreItem(res.data);
          })
          .catch((err) => {
            console.log(err);
          });
      }
      fetchStoreItems();
    } else {
      window.location.href = "/login";
    }
  }, [itemId]);

  return (
    <div className="mx-auto max-w-2xl px-4 py-10 sm:px-6 lg:max-w-7xl lg:px-8">
      <h2 className="text-2xl font-bold tracking-tight text-gray-900">
        Store Item Detail
      </h2>

      {storeItem && (
        <div className="py-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-1 lg:grid-cols-2 xl:gap-x-8">
          <div className="mx-auto">
            <div className="w-4/5 bg-white border border-gray-200 rounded-lg shadow">
              <img
                className="p-8 rounded-t-lg"
                src={storeItem.item.image}
                alt={storeItem.item.title}
              />

              <div className="px-5 pb-5">
                <h5 className="mb-5 text-3xl font-semibold tracking-tight text-gray-900">
                  {storeItem.item.title}
                </h5>

                <div className="flex items-center justify-between">
                  <span className="text-xl font-bold text-gray-900">
                    $ {storeItem.item.opening_bid}
                  </span>
                  <div className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
                    Place your bid
                  </div>
                </div>

                <div className="mt-5">
                  <p className="text-sm text-gray-500">
                    {storeItem.item.description}
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div>
            <h3 className="mb-5 text-2xl font-bold tracking-tight text-gray-900">
              Bidding History
            </h3>

            <div className="relative overflow-x-auto">
              <table className="w-full text-sm text-left rtl:text-right text-gray-500">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                  <tr>
                    <th scope="col" className="px-6 py-3">
                      Bidder
                    </th>
                    <th scope="col" className="px-6 py-3">
                      Bid
                    </th>
                    <th scope="col" className="px-6 py-3">
                      Time
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {storeItem.bids.length > 0 ? (
                    storeItem.bids.map((bid) => (
                      <tr key={bid.id} className="bg-white border-b">
                        <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                          {bid.bidder}
                        </td>
                        <td className="px-6 py-4">$ {bid.amount}</td>
                        <td className="px-6 py-4">
                          {new Date(bid.updated_at).toLocaleString()}
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr className="bg-white border-b">
                      <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                        No bids yet
                      </td>
                      <td className="px-6 py-4"></td>
                      <td className="px-6 py-4"></td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
