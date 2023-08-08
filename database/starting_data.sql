INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Arlo Camera Bundle', 'wireless 4-camera bundle', 399.99, 7, 'static/images/arlo_4_camera.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Bose Soundlink', 'bluetooth portable speaker', 199.99, 20, 'static/images/bose_soundlink_portable_speaker.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Dyson Vacuum', 'cordless vacuum cleaner', 249.99, 10, 'static/images/dyson_v15_cordless_vacuum.jpg', 'Home Appliance');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Hero Camera Bundle', 'action camera bundle', 199.99, 7, 'static/images/hero11_camera_bundle.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('HP Pavillion', '14-inch laptop Core i3', 799.99, 4, 'static/images/hp_pavillion_2in1_14in_Core_i3.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Ninja Foodi', '14-in-1 food processor', 99.99, 15, 'static/images/ninja_foodi_14in1.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Philips Hue', '60-Watt lightbulbs', 49.99, 30, 'static/images/philips_hue_60w.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Playstation 5', 'gaming system', 599.99, 17, 'static/images/playstation5.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Quiet Comfort Headphones', 'wireless bluetooth headphones', 89.99, 6, 'static/images/quiet_comfort_wireless_nose_cancelling.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Roborock', 'S7 MaxV robot vacuum', 999.99, 3, 'static/images/roborock_s7_maxv_robot_vacuum.jpg', 'Home Appliance');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Samsung 75-inch', 'Crystal HD 75-inch TV', 1299.99, 8, 'static/images/samsung_75in.jpg', 'Electronics');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Snowball Cardiods', 'wired cardiods USB', 299.99, 3, 'static/images/snowball_ice_wired_cardiod_usb.jpg', 'Electronics');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
