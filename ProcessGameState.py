import pandas as pd


class ProcessGameState:
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    @staticmethod
    def load_data(file_path):
        # Perform file ingestion and ETL operations if necessary
        data = pd.read_parquet(file_path)
        # Additional ETL operations if required
        return data

    def is_within_boundary(self, x, y, z):
        # Check if the given coordinates fall within the provided boundary
        return 285 <= z <= 421

    def extract_weapon_classes(self):
        # Extract weapon classes from the inventory JSON column
        weapon_classes = self.data['inventory'].apply(lambda x: x.get('class'))
        return weapon_classes

    def common_strategy_light_blue_boundary(self, team, side):
        # Determine if entering via the light blue boundary is a common strategy used by the specified team and side
        filtered_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]
        within_boundary = filtered_data.apply(lambda row: self.is_within_boundary(row['x'], row['y'], row['z']), axis=1)
        return within_boundary.mean()

    def average_entry_timer(self, team, side, site, weapons):
        filtered_data = self.data[(self.data['team'] == team) & (self.data['side'] == side)]
        if 'site' not in filtered_data.columns:
            print("The 'site' column is missing in the data.")
            return None
        filtered_data = filtered_data[filtered_data['site'] == site]
        filtered_data = filtered_data[filtered_data['inventory'].apply(lambda x: any(weapon in x.get('name', '') for weapon in weapons))]
        if filtered_data.empty:
            print("No data found for the specified criteria.")
            return None
        return filtered_data['timer'].mean()





