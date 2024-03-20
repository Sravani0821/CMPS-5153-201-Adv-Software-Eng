import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
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
import axios from "axios";

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
        <Route path="/store/item/:itemId" element={<StoreItemDetail />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
