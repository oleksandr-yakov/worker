ARG ALPINE_VERSION
FROM alpine:${ALPINE_VERSION}
RUN echo ${ALPINE_VERSION}
CMD ["echo", "Hello StackOverflow!"]