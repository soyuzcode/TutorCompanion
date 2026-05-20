package com.keycode.TutorCompanion.service;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import com.keycode.TutorCompanion.dto.ReviewRequest;
import com.keycode.TutorCompanion.model.Review;
import com.keycode.TutorCompanion.model.TutorProfile;
import com.keycode.TutorCompanion.model.User;
import com.keycode.TutorCompanion.repository.ReviewRepository;
import com.keycode.TutorCompanion.repository.TutorProfileRepository;
import com.keycode.TutorCompanion.repository.UserRepository;

@Service
public class ReviewService {

    private final ReviewRepository reviewRepository;
    private final UserRepository userRepository;
    private final TutorProfileRepository tutorProfileRepository;

    public ReviewService(
            ReviewRepository reviewRepository,
            UserRepository userRepository,
            TutorProfileRepository tutorProfileRepository) {
        this.reviewRepository = reviewRepository;
        this.userRepository = userRepository;
        this.tutorProfileRepository = tutorProfileRepository;
    }

    public List<Review> getReviewsByTutor(Long tutorId) {
        if (!userRepository.existsById(tutorId)) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND,
                    "Tutor not found");
        }
        return reviewRepository.findByTutor_Id(tutorId);
    }

    public Review createReview(ReviewRequest request) {
        if (request.rating() == null
                || request.rating() < 1
                || request.rating() > 5) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Rating must be between 1 and 5");
        }

        User tutor = userRepository.findById(request.tutorId())
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND,
                        "Tutor not found"));

        User student = userRepository.findById(request.studentId())
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND,
                        "Student not found"));

        if (tutor.getTutorProfile() == null) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "User is not a tutor");
        }

        if (reviewRepository.existsByTutor_IdAndStudent_Id(
                request.tutorId(),
                request.studentId())) {
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "You already rated this tutor");
        }

        Review review = new Review(
                tutor,
                student,
                request.rating(),
                request.comment());

        reviewRepository.save(review);
        updateTutorRating(tutor.getId());

        return review;
    }

    private void updateTutorRating(Long tutorId) {
        List<Review> reviews = reviewRepository.findByTutor_Id(tutorId);

        double average = reviews.stream()
                .mapToInt(Review::getRating)
                .average()
                .orElse(0.0);

        double rounded = Math.round(average * 10.0) / 10.0;

        TutorProfile profile = tutorProfileRepository.findById(tutorId)
                .orElseThrow();

        profile.setRating(rounded);
        tutorProfileRepository.save(profile);
    }
}
