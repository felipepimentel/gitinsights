// Copyright 2023 The go-github AUTHORS. All rights reserved.
//
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// The ratelimit command demonstrates using the github_ratelimit.SecondaryRateLimitWaiter.
// By using the waiter, the client automatically sleeps and retry requests
// when it hits secondary rate limits.
package main

import (
	"context"
	"fmt"
	// "github.com/google/go-github/v50/github"
	"golang.org/x/oauth2"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	var username string = "felipepimentel"
	var org string = "slimovich"
	var repo string = "https://github.com/slimovich/Realworld-fastapi-gino-template"
	var commitsUrl string = "https://api.github.com/repos/OWNER/REPO/commits"

	ctx := context.Background()
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: os.Getenv("GITHUB_TOKEN")},
	)
	tc := oauth2.NewClient(ctx, ts)

	resp, err := http.Get(commitsUrl)
	if err != nil {
		log.Fatalln(err)
	}

	// ctx := context.Background()
	// ts := oauth2.StaticTokenSource(
	// 	&oauth2.Token{AccessToken: os.Getenv("GITHUB_TOKEN")},
	// )

	// tc := oauth2.NewClient(ctx, ts)
	// client := github.NewClient(tc)

	// stats, _, err := client.Repositories.ListContributorsStats(ctx, org, repo)
	// if _, ok := err.(*github.AcceptedError); ok {
	// 	fmt.Println("scheduled on GitHub side")
	// } else {
	// 	fmt.Println(stats)
	// }

	// repos, _, err := client.Repositories.List(ctx, "felipepimentel", nil)
	// for i, r := range repos {
	// 	fmt.Printf("%v. %v\n", i+1, r)
	// }

	// orgs, _, err := client.Organizations.List(context.Background(), username, nil)
	// if err != nil {
	// 	fmt.Printf("Error: %v\n", err)
	// 	return
	// }

	// for i, organization := range orgs {
	// 	fmt.Printf("%v. %v\n", i+1, organization.GetLogin())
	// }
}
