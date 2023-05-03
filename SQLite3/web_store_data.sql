SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


INSERT INTO `customers` (`id`, `name`, `surname`, `telephone_number`, `email_address`) VALUES
(1, 'Kristina', 'Lileikytė', '+37066998877', 'kristina.lileikyte@gmail.com'),
(2, 'Johny', 'Bravo', '+34761245678', 'johny@bravo.com'),
(3, 'Jack', 'Sparrow', '+380380380', 'jack@sparrow.com');

INSERT INTO `orders` (`id`, `customer_id`, `status`) VALUES
(1, 1, 'in processing'),
(2, 2, 'entered'),
(3, 3, 'delivered');

INSERT INTO `orders_products` (`id`, `order_id`, `product_id`, `products_amount`) VALUES
(8, 1, 2, 2),
(9, 1, 1, 1),
(10, 3, 3, 15),
(11, 2, 1, 3),
(13, 2, 3, 2);

INSERT INTO `products` (`id`, `name`, `description`, `price`, `warranty_period`, `category`, `supplier_id`) VALUES
(1, 'HP Elite Dragonfly G33', 'The HP Dragonfly Folio G3’s excellent design, potent performance, super useful stylus, and decent battery life make the hybrid 2-in-1 one of the best options out there.', 1900, 12, 'PCs', 2),
(2, 'Microsoft Office', 'Microsoft 365 is our cloud-powered productivity platform that includes apps like Microsoft Teams, Word, Excel, PowerPoint, Outlook, OneDrive, and so much more. You can get started with free web and mobile apps or upgrade to a premium plan for access to more apps, storage, and features.', 69.99, 24, 'Software', 1),
(3, 'Magic Mouse', 'Magic Mouse is wireless and rechargeable, with an optimized foot design that lets it glide smoothly across your desk. The Multi-Touch surface allows you to perform simple gestures such as swiping between web pages and scrolling through documents.', 99, 18, 'Accessories', 3);

INSERT INTO `suppliers` (`id`, `name`, `contact`, `telephone_number`, `email`) VALUES
(1, 'Microsoft', 'Bill Gates', '+37012346789', 'bill.gates@microsoft.com'),
(2, 'HP', 'Enrique Lores', '+37012346789', 'enrique.lores@hp.com'),
(3, 'Apple', 'Tim Cook', '+37012346789', 'tim.cook@apple.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
