import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import moment from "moment";

export default function StoreItemDetail() {
  const { itemId } = useParams();
  const [storeItem, setStoreItem] = useState(null);
  const [bidAmount, setBidAmount] = useState(0.0);
  const [userData, setUserData] = useState(null);
  const [wishList, setWishList] = useState(false);

  async function fetchStoreItems() {
    await axios
      .get(`/item/store/${itemId}/`)
      .then((res) => {
        setStoreItem(res.data);
        console.log(res.data);
        setBidAmount(res.data.item.opening_bid);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function fetchWishList() {
    await axios
      .get(`/item/store/${itemId}/wishlist/`)
      .then((res) => {
        setWishList(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function handleSell() {
    await axios
      .post(`/item/store/${itemId}/sell/`)
      .then((res) => {
        fetchStoreItems();
        fetchStoreItems();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  const handleWishList = async () => {
    await axios
      .post(`/item/store/${itemId}/wishlist/`)
      .then((res) => {
        fetchWishList();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handlePlaceBid = async () => {
    await axios
      .post(`/item/store/${itemId}/bid/`, {
        amount: bidAmount,
      })
      .then((res) => {
        fetchStoreItems();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      setUserData(JSON.parse(localStorage.getItem("user_data")));
      fetchStoreItems();
      fetchWishList();
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

                  {userData.type === "seller" ? (
                    <button className="text-white bg-pink-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center opacity-50 cursor-not-allowed">
                      Can't Wishlist
                    </button>
                  ) : wishList ? (
                    <button className="text-white bg-pink-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center opacity-50 cursor-not-allowed">
                      Wishlisted
                    </button>
                  ) : (
                    <button
                      type="button"
                      className="text-white bg-pink-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                      onClick={handleWishList}
                    >
                      Wishlist
                    </button>
                  )}

                  {userData.type === "seller" ? (
                    <div
                      type="button"
                      className="text-white bg-blue-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center opacity-50 cursor-not-allowed"
                    >
                      Can't Bid
                    </div>
                  ) : moment(storeItem.item.auction_end).isBefore(
                      new Date(),
                    ) ? (
                    <div
                      type="button"
                      className="text-white bg-blue-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center opacity-50 cursor-not-allowed"
                    >
                      Auction Ended
                    </div>
                  ) : (
                    <div
                      type="button"
                      className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                      onClick={() => {
                        document.getElementById("currency-input").focus();
                      }}
                    >
                      Place your bid
                    </div>
                  )}
                </div>

                <div className="mt-5">
                  <p className="text-sm text-gray-500">
                    {storeItem.item.description}
                  </p>

                  <span className="block mt-5 text-sm">
                    Auction Ends:{" "}
                    <strong>
                      {moment(storeItem.item.auction_end).format(
                        "MMMM Do YYYY, h:mm:ss a",
                      )}
                    </strong>
                  </span>

                  <span className="block mt-5 text-sm">
                    Seller: <strong>{storeItem.item.seller}</strong>
                  </span>

                  <span className="block mt-5 text-sm">
                    Contact: <strong>{storeItem.item.contact}</strong>
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div>
            <h3 className="mb-5 text-2xl font-bold tracking-tight text-gray-900">
              Place Your Bid
            </h3>

            {userData.type === "bidder" ? (
              <div className="bg-white border border-gray-200 rounded-lg shadow p-8">
                <form class="max-w-full mx-auto flex">
                  <label
                    for="currency-input-1"
                    class="mb-2 text-sm font-medium text-gray-900 sr-only"
                  >
                    Your Bid
                  </label>
                  <div class="relative w-full">
                    <div class="absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none">
                      <svg
                        class="w-4 h-4 text-gray-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 20 16"
                      >
                        <path
                          stroke="currentColor"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M5 2a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1M2 5h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm8 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z"
                        />
                      </svg>
                    </div>
                    <input
                      type="number"
                      id="currency-input"
                      class="block p-2.5 w-full z-20 ps-10 text-sm text-gray-900 bg-gray-50 rounded-s-lg border-e-gray-50 border-e-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                      placeholder="Enter amount"
                      required
                      value={bidAmount}
                      onChange={(e) => setBidAmount(e.target.value)}
                    />
                  </div>
                  <button
                    id="dropdown-currency-button"
                    data-dropdown-toggle="dropdown-currency"
                    class="flex-shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-gray-300 rounded-e-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100"
                    type="button"
                  >
                    <svg
                      fill="none"
                      aria-hidden="true"
                      class="h-4 w-4 me-2"
                      viewBox="0 0 20 15"
                    >
                      <rect
                        width="19.6"
                        height="14"
                        y=".5"
                        fill="#fff"
                        rx="2"
                      />
                      <mask
                        id="a"
                        width="20"
                        height="15"
                        x="0"
                        y="0"
                        maskUnits="userSpaceOnUse"
                      >
                        <rect
                          width="19.6"
                          height="14"
                          y=".5"
                          fill="#fff"
                          rx="2"
                        />
                      </mask>
                      <g mask="url(#a)">
                        <path
                          fill="#D02F44"
                          fill-rule="evenodd"
                          d="M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z"
                          clip-rule="evenodd"
                        />
                        <path fill="#46467F" d="M0 .5h8.4v6.533H0z" />
                        <g filter="url(#filter0_d_343_121520)">
                          <path
                            fill="url(#paint0_linear_343_121520)"
                            fill-rule="evenodd"
                            d="M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z"
                            clip-rule="evenodd"
                          />
                        </g>
                      </g>
                      <defs>
                        <linearGradient
                          id="paint0_linear_343_121520"
                          x1=".933"
                          x2=".933"
                          y1="1.433"
                          y2="6.1"
                          gradientUnits="userSpaceOnUse"
                        >
                          <stop stop-color="#fff" />
                          <stop offset="1" stop-color="#F0F0F0" />
                        </linearGradient>
                        <filter
                          id="filter0_d_343_121520"
                          width="6.533"
                          height="5.667"
                          x=".933"
                          y="1.433"
                          color-interpolation-filters="sRGB"
                          filterUnits="userSpaceOnUse"
                        >
                          <feFlood
                            flood-opacity="0"
                            result="BackgroundImageFix"
                          />
                          <feColorMatrix
                            in="SourceAlpha"
                            result="hardAlpha"
                            values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                          />
                          <feOffset dy="1" />
                          <feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0" />
                          <feBlend
                            in2="BackgroundImageFix"
                            result="effect1_dropShadow_343_121520"
                          />
                          <feBlend
                            in="SourceGraphic"
                            in2="effect1_dropShadow_343_121520"
                            result="shape"
                          />
                        </filter>
                      </defs>
                    </svg>
                    USD
                  </button>
                  <div
                    id="dropdown-currency"
                    class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-36"
                  >
                    <ul
                      class="py-2 text-sm text-gray-700"
                      aria-labelledby="dropdown-currency-button"
                    >
                      <li>
                        <button
                          type="button"
                          class="inline-flex w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          <div class="inline-flex items-center">
                            <svg
                              fill="none"
                              aria-hidden="true"
                              class="h-4 w-4 me-2"
                              viewBox="0 0 20 15"
                            >
                              <rect
                                width="19.6"
                                height="14"
                                y=".5"
                                fill="#fff"
                                rx="2"
                              />
                              <mask
                                id="a"
                                width="20"
                                height="15"
                                x="0"
                                y="0"
                                maskUnits="userSpaceOnUse"
                              >
                                <rect
                                  width="19.6"
                                  height="14"
                                  y=".5"
                                  fill="#fff"
                                  rx="2"
                                />
                              </mask>
                              <g mask="url(#a)">
                                <path
                                  fill="#D02F44"
                                  fill-rule="evenodd"
                                  d="M19.6.5H0v.933h19.6V.5zm0 1.867H0V3.3h19.6v-.933zM0 4.233h19.6v.934H0v-.934zM19.6 6.1H0v.933h19.6V6.1zM0 7.967h19.6V8.9H0v-.933zm19.6 1.866H0v.934h19.6v-.934zM0 11.7h19.6v.933H0V11.7zm19.6 1.867H0v.933h19.6v-.933z"
                                  clip-rule="evenodd"
                                />
                                <path fill="#46467F" d="M0 .5h8.4v6.533H0z" />
                                <g filter="url(#filter0_d_343_121520)">
                                  <path
                                    fill="url(#paint0_linear_343_121520)"
                                    fill-rule="evenodd"
                                    d="M1.867 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.866 0a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM7.467 1.9a.467.467 0 11-.934 0 .467.467 0 01.934 0zM2.333 3.3a.467.467 0 100-.933.467.467 0 000 .933zm2.334-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm1.4.467a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.934 0 .467.467 0 01.934 0zm-2.334.466a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.466a.467.467 0 11-.933 0 .467.467 0 01.933 0zM1.4 4.233a.467.467 0 100-.933.467.467 0 000 .933zm1.4.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zm1.4.467a.467.467 0 100-.934.467.467 0 000 .934zM6.533 4.7a.467.467 0 11-.933 0 .467.467 0 01.933 0zM7 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.933 0 .467.467 0 01.933 0zM3.267 6.1a.467.467 0 100-.933.467.467 0 000 .933zm-1.4-.467a.467.467 0 11-.934 0 .467.467 0 01.934 0z"
                                    clip-rule="evenodd"
                                  />
                                </g>
                              </g>
                              <defs>
                                <linearGradient
                                  id="paint0_linear_343_121520"
                                  x1=".933"
                                  x2=".933"
                                  y1="1.433"
                                  y2="6.1"
                                  gradientUnits="userSpaceOnUse"
                                >
                                  <stop stop-color="#fff" />
                                  <stop offset="1" stop-color="#F0F0F0" />
                                </linearGradient>
                                <filter
                                  id="filter0_d_343_121520"
                                  width="6.533"
                                  height="5.667"
                                  x=".933"
                                  y="1.433"
                                  color-interpolation-filters="sRGB"
                                  filterUnits="userSpaceOnUse"
                                >
                                  <feFlood
                                    flood-opacity="0"
                                    result="BackgroundImageFix"
                                  />
                                  <feColorMatrix
                                    in="SourceAlpha"
                                    result="hardAlpha"
                                    values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                                  />
                                  <feOffset dy="1" />
                                  <feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0" />
                                  <feBlend
                                    in2="BackgroundImageFix"
                                    result="effect1_dropShadow_343_121520"
                                  />
                                  <feBlend
                                    in="SourceGraphic"
                                    in2="effect1_dropShadow_343_121520"
                                    result="shape"
                                  />
                                </filter>
                              </defs>
                            </svg>
                            USD
                          </div>
                        </button>
                      </li>
                    </ul>
                  </div>
                </form>

                <div className="mt-5">
                  {moment(storeItem.item.auction_end).isBefore(new Date()) ? (
                    <button className="w-full bg-blue-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-white text-sm px-5 py-2.5 text-center opacity-50 cursor-not-allowed">
                      Auction Ended
                    </button>
                  ) : (
                    <button
                      className="w-full bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-white text-sm px-5 py-2.5 text-center"
                      onClick={handlePlaceBid}
                    >
                      Place Bid
                    </button>
                  )}
                </div>
              </div>
            ) : (
              <div className="bg-white border border-gray-200 rounded-lg shadow p-8">
                {storeItem.item.is_sold ? (
                  <button className="text-white bg-red-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center w-full opacity-50 cursor-not-allowed">
                    Item sold
                  </button>
                ) : moment(storeItem.item.auction_end).isBefore(new Date()) ? (
                  <button
                    className="text-white bg-red-700 focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-5 py-2.5 text-center w-full"
                    onClick={handleSell}
                  >
                    Sell to the highest bidder
                  </button>
                ) : (
                  <p className="text-gray-500">Only bidders can place a bid</p>
                )}
              </div>
            )}

            <h3 className="my-5 text-2xl font-bold tracking-tight text-gray-900">
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
                          {new Date(bid.created_at).toLocaleString("en-US", {
                            year: "numeric",
                            month: "short",
                            day: "numeric",
                            hour: "numeric",
                            minute: "numeric",
                          })}
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
