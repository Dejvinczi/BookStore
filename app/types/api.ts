export interface ApiError {
  response?: {
    status: number;
    data: {
      detail?: string;
      [key: string]: string | undefined;
    };
  };
  message: string;
}
