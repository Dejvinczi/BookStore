export interface Author {
  id: number;
  firstName: string;
  lastName: string;
  dateOfBirth: Date;
}

export interface AuthorDetail extends Author {}

export interface AuthorApiResponse {
  count: number;
  next: string;
  previous: string;
  results: Author[];
}

export interface AuthorDetailApiResponse extends AuthorDetail {}
