import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import axios from "axios";
import Login from "./components/auth/login";
import Register from "./components/auth/register";
import RegisterAsSeller from "./components/auth/register-as-seller";
import RegisterAsBidder from "./components/auth/register-as-bidder";
import Logout from "./components/auth/logout";
import Navbar from "./components/navbar";
import Home from "./components/home";
import Page404 from "./components/page-404";
import StoreHome from "./components/store/store-home";
import StoreItemDetail from "./components/store/store-item-detail";
import StoreItemCreate from "./components/store/store-item-create";
import LottreyHome from "./components/lottery/lottery-home";
import LotteryItemCreate from "./components/lottery/lottery-item-create";
import LotteryItemDetail from "./components/lottery/lottery-item-detail";
import Contact from "./components/contact";
import SellerDashboard from "./components/dashboard/seller/dashboard";
import SellerDashboardStore from "./components/dashboard/seller/store";
import SellerDashboardLottery from "./components/dashboard/seller/lottery";
import BidderDashboard from "./components/dashboard/bidder/dashboard";
import Notifications from "./components/notifications";

axios.defaults.baseURL = "http://127.0.0.1:8000";
axios.defaults.headers.post["Content-Type"] = "application/json";

function App() {
  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      axios.defaults.headers.common["Authorization"] =
        `Bearer ${localStorage.getItem("access_token")}`;

      if (localStorage.getItem("user_data") === null) {
        axios
          .get("/auth/user/")
          .then((res) => {
            localStorage.setItem("user_data", JSON.stringify(res.data));
          })
          .catch((err) => {
            console.log(err);
          });
      }
    }
  }, []);

  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="*" element={<Page404 />} />
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/register/seller" element={<RegisterAsSeller />} />
        <Route path="/register/bidder" element={<RegisterAsBidder />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/store" element={<StoreHome />} />
        <Route path="/store/create" element={<StoreItemCreate />} />
        <Route path="/store/item/:itemId" element={<StoreItemDetail />} />
        <Route path="/lottery" element={<LottreyHome />} />
        <Route path="/lottery/create" element={<LotteryItemCreate />} />
        <Route path="/lottery/item/:itemId" element={<LotteryItemDetail />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/dashboard/seller" element={<SellerDashboard />} />
        <Route
          path="/dashboard/seller/store"
          element={<SellerDashboardStore />}
        />
        <Route
          path="/dashboard/seller/lottery"
          element={<SellerDashboardLottery />}
        />
        <Route path="/dashboard/bidder" element={<BidderDashboard />} />
        <Route path="/notifications" element={<Notifications />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
