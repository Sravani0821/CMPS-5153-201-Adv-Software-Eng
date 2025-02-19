import moment from "moment";

export default function LotteryItemCard({ item }) {
  return (
    <div class="group relative">
      <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-100 lg:aspect-none group-hover:opacity-75">
        <a href={`/lottery/item/${item.id}`}>
          <img
            src={item.image}
            alt={item.title}
            class="h-full w-full object-cover object-center lg:h-full lg:w-full"
          />
        </a>
      </div>
      <div class="mt-4">
        <h3 class="text-sm text-gray-700">
          <a href={`/lottery/item/${item.id}`} class="font-bold text-gray-900">
            {item.title}
          </a>
        </h3>
        <p class="mt-1 text-sm text-gray-500">$ {item.bid}</p>
        <p class="mt-1 text-sm text-gray-500">
          Lottery ends {moment(item.auction_end).fromNow()}
        </p>
      </div>
    </div>
  );
}
