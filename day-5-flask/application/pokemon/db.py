import numpy as np
import pandas as pd


class KNNSearchEngine:
    def __init__(self, data_path, features=["hp", "attack", "defense", "sp_atk", "sp_def", "speed" ], distance_function='euclidean'):
        self.df = pd.read_csv(data_path)
        self.features = features
        self.X = self.df[features].values
        self.X_scaled = self.standardize(self.X)
        self.distance_function = self.get_distance_function(distance_function)
        self.inv_cov_matrix = np.linalg.inv(np.cov(self.X_scaled.T))
        
    def standardize(self, data):
        mean = data.mean(axis=0)
        std = data.std(axis=0)
        return (data - mean) / std

    def euclidean_distance(self, a, b):
        return np.sqrt(np.sum((a - b) ** 2, axis=1))
    
    def manhattan_distance(self, a, b):
        return np.sum(np.abs(a - b), axis=1)
    
    def mahalanobis_distance(self, a, b):
        delta = a - b
        return np.sqrt(np.sum(delta @ self.inv_cov_matrix * delta, axis=1))

    def get_distance_function(self, name):
        if name == 'euclidean':
            return self.euclidean_distance
        elif name == 'manhattan':
            return self.manhattan_distance
        elif name == 'mahalanobis':
            return self.mahalanobis_distance
        else:
            raise ValueError(f"Unsupported distance function: {name}")

    def knn_search(self, query, k=5):
        distances = self.distance_function(self.X_scaled, query)
        nearest_indices = distances.argsort()[:k]
        return nearest_indices

    def search_by_name(self, pokemon_name, n_neighbors=5):
        indexes = self.df[self.df['name'].str.contains(pokemon_name, case=False)].index
        if len(indexes) > 0:
            pokemon_index = indexes[0]
            query = self.X_scaled[pokemon_index].reshape(1, -1)
            neighbors_indices = self.knn_search(query, k=n_neighbors)
            return self.df.loc[neighbors_indices].to_dict("records")
        else:
            return []

    def find_similar_pokemon(self, query_string, n_neighbors=5):
        # Qui chiamare il metodo per applicare KNN
        pass  

    def __repr__(self):
        return f"KNNSearchEngine(data_path={self.df}, features={self.features}, distance_function={self.distance_function.__name__})"
    
    def __getitem__(self, index):
        return self.df.iloc[index]
    
    def __len__(self):
        return len(self.df)
    
    def __call__(self, pokemon_name, n_neighbors=5):
        return self.search_by_name(pokemon_name, n_neighbors)
