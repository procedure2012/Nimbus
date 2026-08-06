# Nimbus Development Repository

> 🚧 **Development Branch** - main development repository for Nimbus

## About Nimbus

Nimbus offers a unified API over S3, GCS and Azure Blob storage.

## 🔧 Development Status

This repository is under active development. Many features are TODO.

### 🔴 High Priority TODOs

- Core functionality is still being implemented across modules.

### 📝 Complete TODO List

- [ ] **nimbus/backends/gcs.py:3** - implement resumable uploads
- [ ] **nimbus/backends/s3.py:3** - use multipart upload for large objects
- [ ] **nimbus/backends/s3.py:4** - add server-side encryption headers
- [ ] **nimbus/backends/s3.py:8** - support ranged/partial downloads
- [ ] **nimbus/cache/lru.py:3** - make the cache thread-safe
- [ ] **nimbus/cache/lru.py:4** - add size-based eviction in bytes

## 🤝 Contributing

1. Pick a TODO item from the list above
2. Implement the functionality
3. Update this README when TODOs are completed
