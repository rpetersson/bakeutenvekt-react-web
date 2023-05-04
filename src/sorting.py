import json

json_str = '''{
    "ingredients": [
        {
            "density": 0.593,
            "name": "All-purpose flour"
        },
        {
            "density": 0.849,
            "name": "Granulated sugar"
        },
        {
            "density": 0.911,
            "name": "Butter"
        },
        {
            "density": 1.03,
            "name": "Eggs"
        },
        {
            "density": 1.03,
            "name": "Milk"
        },
        {
            "density": 0.85,
            "name": "Brown sugar"
        },
        {
            "density": 0.641,
            "name": "Baking powder"
        },
        {
            "density": 1.202,
            "name": "Salt"
        },
        {
            "density": 2.159,
            "name": "Baking soda"
        },
        {
            "density": 1.065,
            "name": "Vanilla extract"
        },
        {
            "density": 0.59,
            "name": "Cocoa powder"
        },
        {
            "density": 1.03,
            "name": "Yogurt"
        },
        {
            "density": 0.97,
            "name": "Cream cheese"
        },
        {
            "density": 0.57,
            "name": "Cornstarch"
        },
        {
            "density": 1.42,
            "name": "Honey"
        },
        {
            "density": 0.56,
            "name": "Powdered sugar"
        },
        {
            "density": 0.92,
            "name": "Vegetable oil"
        },
        {
            "density": 0.67,
            "name": "Almond flour"
        },
        {
            "density": 1.37,
            "name": "Maple syrup"
        },
        {
            "density": 0.82,
            "name": "Dark chocolate chips"
        },
        {
            "density": 0.925,
            "name": "White chocolate chips"
        },
        {
            "density": 1.01,
            "name": "Heavy cream"
        },
        {
            "density": 1.48,
            "name": "Unsweetened chocolate"
        },
        {
            "density": 1.01,
            "name": "Sour cream"
        },
        {
            "density": 0.59,
            "name": "Bread flour"
        },
        {
            "density": 0.9,
            "name": "Semi-sweet chocolate chips"
        },
        {
            "density": 0.51,
            "name": "Cake flour"
        },
        {
            "density": 1.33,
            "name": "Light corn syrup"
        },
        {
            "density": 1.01,
            "name": "Peanut butter"
        },
        {
            "density": 0.57,
            "name": "Whole wheat flour"
        },
        {
            "density": 1.46,
            "name": "Molasses"
        },
        {
            "density": 0.92,
            "name": "Shortening"
        },
        {
            "density": 0.55,
            "name": "Sliced almonds"
        },
        {
            "density": 0.56,
            "name": "Confectioners' sugar"
        },
        {
            "density": 1.01,
            "name": "Buttermilk"
        },
        {
            "density": 1.04,
            "name": "Cinnamon"
        },
        {
            "density": 0.9,
            "name": "Dark brown sugar"
        },
        {
            "density": 1.08,
            "name": "Pumpkin puree"
        },
        {
            "density": 0.6,
            "name": "Pecans"
        },
        {
            "density": 0.89,
            "name": "Canned coconut milk"
        },
        {
            "density": 1.01,
            "name": "White vinegar"
        },
        {
            "density": 0.7,
            "name": "Graham cracker crumbs"
        },
        {
            "density": 0.43,
            "name": "Rolled oats"
        },
        {
            "density": 0.54,
            "name": "Cornmeal"
        },
        {
            "density": 0.43,
            "name": "Panko bread crumbs"
        },
        {
            "density": 0.79,
            "name": "Raisins"
        },
        {
            "density": 0.92,
            "name": "Coconut oil"
        },
        {
            "density": 1.33,
            "name": "Corn syrup"
        },
        {
            "density": 1.04,
            "name": "Ground cinnamon"
        },
        {
            "density": 0.92,
            "name": "Margarine"
        },
        {
            "density": 0.64,
            "name": "Walnuts"
        },
        {
            "density": 0.49,
            "name": "Peanuts"
        },
        {
            "density": 0.7,
            "name": "Pumpkin pie spice"
        },
        {
            "density": 0.72,
            "name": "Chocolate sprinkles"
        },
        {
            "density": 1.04,
            "name": "Almond extract"
        },
        {
            "density": 1,
            "name": "Butter flavoring"
        },
        {
            "density": 1.13,
            "name": "Ground ginger"
        },
        {
            "density": 0.95,
            "name": "Ground nutmeg"
        },
        {
            "density": 1.06,
            "name": "Ground cloves"
        },
        {
            "density": 0.85,
            "name": "Ground allspice"
        },
        {
            "density": 0.78,
            "name": "Ginger snaps"
        },
        {
            "density": 0.65,
            "name": "Pumpkin seeds"
        },
        {
            "density": 0.95,
            "name": "Dark rum"
        },
        {
            "density": 1.05,
            "name": "Lemon juice"
        },
        {
            "density": 0.54,
            "name": "Lemon zest"
        },
        {
            "density": 1.05,
            "name": "Lime juice"
        },
        {
            "density": 0.54,
            "name": "Lime zest"
        },
        {
            "density": 1.05,
            "name": "Orange juice"
        },
        {
            "density": 0.7,
            "name": "Orange zest"
        },
        {
            "density": 1.04,
            "name": "Lemon extract"
        },
        {
            "density": 1.05,
            "name": "Orange extract"
        },
        {
            "density": 1.03,
            "name": "Mint extract"
        },
        {
            "density": 0.6,
            "name": "Pistachios"
        },
        {
            "density": 1.57,
            "name": "Ground cardamom"
        },
        {
            "density": 0.63,
            "name": "Graham crackers"
        },
        {
            "density": 0.79,
            "name": "Chopped dates"
        },
        {
            "density": 0.35,
            "name": "Shredded coconut"
        },
        {
            "density": 0.42,
            "name": "Sesame seeds"
        },
        {
            "density": 0.67,
            "name": "Poppy seeds"
        },
        {
            "density": 0.52,
            "name": "Black sesame seeds"
        },
        {
            "density": 1.57,
            "name": "Baking chocolate"
        },
        {
            "density": 0.85,
            "name": "Chocolate chips"
        },
        {
            "density": 0.641,
            "name": "Active dry yeast"
        },
        {
            "density": 0.641,
            "name": "Instant yeast"
        },
        {
            "density": 0.527,
            "name": "Bread improver"
        },
        {
            "density": 0.55,
            "name": "Cake improver"
        },
        {
            "density": 0.567,
            "name": "Corn flour"
        },
        {
            "density": 0.593,
            "name": "Rice flour"
        },
        {
            "density": 0.57,
            "name": "Potato flour"
        },
        {
            "density": 0.567,
            "name": "Tapioca flour"
        },
        {
            "density": 0.5,
            "name": "Xanthan gum"
        },
        {
            "density": 0.5,
            "name": "Guar gum"
        },
        {
            "density": 0.98,
            "name": "Cream of tartar"
        },
        {
            "density": 0.56,
            "name": "Meringue powder"
        },
        {
            "density": 0.95,
            "name": "Gelatin"
        },
        {
            "density": 1.66,
            "name": "Citric acid"
        },
        {
            "density": 0.85,
            "name": "White sugar"
        }
    ]
}'''

data = json.loads(json_str)

data['ingredients'].sort(key=lambda x: x['name'])

sorted_json_str = json.dumps(data, indent=4)

print(sorted_json_str)