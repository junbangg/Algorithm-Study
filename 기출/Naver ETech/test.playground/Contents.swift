import Foundation

/**
 CatImageCellModel:
    placeholderImage
    - func fetchCatImage(@escaping completion () -> Result<Image, Error>)
*/
/**
 DIspatchQueue.mainSync {
    이 안에서 fetchCatImage를 2번 호출해서
 completion이 나왔을때 set 하고
 안되면 여기서 그냥 placeholderImage set
 }
 */
final class CatImageCell: UICollectionViewCell {
    
    private var imageView: UIImageView!
    
    convenience init(imageView: UIImageView) {
        self.init()
        
        self.imageView = imageView
    }
    
    func set(model: CatImageCellModel) {
        
        // dispatch main queue async
        DispatchQueue.main.async {
            var count = 0
            model.fetchCatImage() { [weak self] completion in
                switch completion {
                case .failure(let error):
                    if counter <
                    return error.timeout
                case .success(let data):
                    self?.imageView = data
                }
            }
            
        }
        // if fails * watchout for optional
        self.imageView = model.placeholderImage
    }
