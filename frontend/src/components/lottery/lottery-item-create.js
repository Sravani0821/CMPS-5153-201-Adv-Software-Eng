import React, { useState, useEffect } from "react";
import axios from "axios";

export default function LotteryItemCreate() {
  const [errorMessage, setErrorMessage] = useState(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [image, setImage] = useState(null);
  const [bid, setBid] = useState("");
  const [contact, setContact] = useState("");
  const [auctionEnd, setAuctionEnd] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("image", image, image.name);
    formData.append("bid", bid);
    formData.append("contact", contact);
    formData.append("auction_end", auctionEnd);

    try {
      const response = await axios.post("/item/lottery/new/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }

    window.location.href = "/lottery/";
  };

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      if (JSON.parse(localStorage.getItem("user_data")).type === "bidder") {
        setErrorMessage("Only sellers are allowed to create lottery items.");
      }
    } else {
      window.location.href = "/login";
    }
  }, []);

  return (
    <>
      {errorMessage ? (
        <div className="text-center text-red-500">{errorMessage}</div>
      ) : (
        <div className="my-10 px-5">
          <form
            className="pt-11 pb-5 px-5 w-full max-w-md m-auto bg-gray-100 rounded-lg shadow-lg"
            onSubmit={handleSubmit}
          >
            <h1 className="text-center text-2xl font-bold text-gray-900 mb-6">
              Create new lottery item
            </h1>
            <div className="mb-6">
              <label
                for="title"
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Title
              </label>
              <input
                type="text"
                id="title"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                placeholder="Title"
                required
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                for="description"
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Description
              </label>
              <textarea
                type="text"
                id="description"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                placeholder="Description"
                required
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                class="block mb-2 text-sm font-medium text-gray-900"
                for="file_input"
              >
                Image
              </label>
              <input
                class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none"
                id="file_input"
                type="file"
                required
                onChange={(e) => setImage(e.target.files[0])}
              />
            </div>
            <div className="mb-6">
              <label
                for="bid"
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Bid
              </label>
              <input
                type="number"
                id="bid"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                placeholder="Bid"
                required
                value={bid}
                onChange={(e) => setBid(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                for="contact"
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Contact
              </label>
              <input
                type="text"
                id="contact"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                placeholder="Contact"
                required
                value={contact}
                onChange={(e) => setContact(e.target.value)}
              />
            </div>
            <div className="mb-6">
              <label
                for="auction_end"
                className="block mb-2 text-sm font-medium text-gray-900"
              >
                Auction end
              </label>
              <input
                type="datetime-local"
                id="auction_end"
                className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                placeholder="Auction end"
                required
                value={auctionEnd}
                onChange={(e) => setAuctionEnd(e.target.value)}
              />
            </div>

            <button
              type="submit"
              className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
            >
              Post new item
            </button>
          </form>
        </div>
      )}
    </>
  );
}
