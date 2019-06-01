python get_captures.py ../data/src/pd_items.json ../data/captures.json;
python get_collections.py ../data/src/pd_items.json ../data/collections.json ../data/item_collections.json;
python get_color_data.py ../data/captures.json ../img/items/ ../data/item_hsl.json 3;
python get_colors.py ../data/item_hsl.json ../data/colors.json ../data/item_colors.json;
python get_dates.py ../data/src/pd_items.json ../data/centuries.json ../data/item_centuries.json century;
python get_genres.py ../data/src/pd_items.json ../data/genres.json ../data/item_genres.json;
python stitch_images.py ../data/ ../img/items/ ../img/ 200 5 5 default 50 20 3 80000
python stitch_images.py ../data/ ../img/items/ ../img/ 200 5 5 centuries 50 20 3 80000
python stitch_images.py ../data/ ../img/items/ ../img/ 200 5 5 collections 50 20 3 80000
python stitch_images.py ../data/ ../img/items/ ../img/ 200 5 5 colors 50 20 3 80000
python stitch_images.py ../data/ ../img/items/ ../img/ 200 5 5 genres 50 20 3 80000
python generate_metadata.py ../data/src/pd_items.json ../js/items/ 5;
python generate_labels.py ../data/ ../js/labels.json 200 5 50 20 3;
python generate_coordinates.py ../data/ ../js/coords.json 200 5 5 50 20 3;

