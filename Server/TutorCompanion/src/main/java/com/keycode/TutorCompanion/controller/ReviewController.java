package com.keycode.TutorCompanion.controller;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.keycode.TutorCompanion.dto.ReviewRequest;
import com.keycode.TutorCompanion.model.Review;
import com.keycode.TutorCompanion.service.ReviewService;

@RestController
@RequestMapping("/reviews")
public class ReviewController {

    private final ReviewService reviewService;

    public ReviewController(ReviewService reviewService) {
        this.reviewService = reviewService;
    }

    @GetMapping
    public ResponseEntity<List<Review>> getReviewsByTutor(
            @RequestParam Long tutorId) {
        return ResponseEntity.ok(
                reviewService.getReviewsByTutor(tutorId));
    }

    @PostMapping
    public ResponseEntity<Review> createReview(
            @RequestBody ReviewRequest request) {
        return ResponseEntity.ok(
                reviewService.createReview(request));
    }
}
