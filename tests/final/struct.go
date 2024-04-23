package main

type JobResponse struct {
	JobId   int64
	Status  bool
	Stipend float64
	Remarks string
}

func main() {
	var a JobResponse
	a.JobId = 22
	a.Status = true
	a.Stipend = 225000.0
	a.Remarks = "Job is great!"
	printf(a.JobId)
	printf(a.Status)
	printf(a.Stipend)
	printf(a.Remarks)

	return
}
