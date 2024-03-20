import SellerLogo from "../../images/seller.webp";
import BidderLogo from "../../images/bidder.webp";

export default function Register() {
  return (
    <div className="pt-10 pb-5 px-5 w-full max-w-md m-auto bg-gray-100 rounded-lg shadow-lg">
      <h1 className="text-center text-2xl font-bold text-gray-900 mb-6">
        Register as
      </h1>
      <div className="mb-6">
        <div className="flex items-center justify-center space-x-5">
          <div className="text-center">
            <img src={SellerLogo} alt="Seller" className="w-20 h-20" />
            <a
              href="/register/seller"
              className="text-blue-500 hover:underline"
            >
              Seller
            </a>
          </div>

          <div className="text-center">
            <img src={BidderLogo} alt="Bidder" className="w-20 h-20" />
            <a
              href="/register/bidder"
              className="text-blue-500 hover:underline"
            >
              Bidder
            </a>
          </div>
        </div>
      </div>

      <p className="text-center mt-10">
        Already have an account?{" "}
        <a href="/login" className="text-blue-500 hover:underline">
          Login
        </a>
      </p>
    </div>
  );
}
