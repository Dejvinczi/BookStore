export interface Genre {
  id: number;
  name: string;
}

export interface GenreDetail extends Genre {}

export interface GenreApiResponse {
  count: number;
  next: string;
  previous: string;
  results: Genre[];
}

export interface GenreDetailApiResponse extends GenreDetail {}
